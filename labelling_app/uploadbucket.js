//load Max Api
const maxAPI = require('max-api');

// The ID of your GCS bucket
const bucketName = 'database-sound-objects';

// The path to your file to upload
var audioFilePath = '';

// The path to your file to upload
var jsonFilePath = '';

// The new ID for your GCS Audio file
var destFileName = '';

// The new ID for your GCS Json file

var destJsonName = '';

// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// Creates a client from a Google service account key
const storage = new Storage({keyFilename: '*'});

maxAPI.addHandler("jsonPath", (dir) => {
		jsonFilePath = (`${dir}`);
		//maxAPI.outlet(jsonFilePath);
		console.log(`Json file path is ${jsonFilePath}`)
	});

maxAPI.addHandler("destJsonName", (dir) => {
		destJsonName = (`${dir}`);
		//maxAPI.outlet(destJsonName);
		console.log(`Destination Json file path is ${destJsonName}`)
	});

maxAPI.addHandler("audioFilePath", (dir) => {
		audioFilePath = (`${dir}`);
		//maxAPI.outlet(audioFilePath);
		console.log(`Audio file path is ${audioFilePath}`)
	});
	
maxAPI.addHandler("destFileName", (dir) => {
		destFileName = (`${dir}`);
		//maxAPI.outlet(destFileName);
		console.log(`DestfileName is ${destFileName}`)
	});

maxAPI.addHandler("load", (...args) => {

	async function uploadFile() {
  	const options = {
    	destination: destFileName
  	};
  	const options_json = {
  	  destination: destJsonName
  	};

  	await storage.bucket(bucketName).upload(audioFilePath, options);
  	
  	console.log(`${destFileName} uploaded to ${bucketName}`);
	
	await storage.bucket(bucketName).upload(jsonFilePath, options_json);
    console.log(`${destJsonName} uploaded to ${bucketName}`);
	maxAPI.outlet(`Success:  Success: ${destFileName} and ${destJsonName} uploaded to dataset`);
}
uploadFile().catch(console.error);
});
