# SCHAEFFER
**Authors:** Maurizio Berta & Daniele Ghisi

The SCHAEFFER dataset (Spectro-morphogical Corpus of Human-annotated Audio with Electroacoustic Features For Experimental Research) is a compilation of 1000 raw audio files accompanied by human annotations and morphological acoustic features. The audio files adhere to the concept of Sound Objects introduced by Pierre Schaeffer, a framework for the analysis and creation of sound that focuses on its typological and morphological characteristics. Inside the dataset, the annotations are provided in the form of free text, while the labels are pre-chosen from a list of classes, making the sound description fit into a suitable framework for digital analysis.

## Dataset Access

The dataset is available on the following platforms:

- **[Hugging Face](https://huggingface.co/datasets/dbschaeffer/SCHAEFFER)**
- **[Kaggle](https://www.kaggle.com/datasets/maurizioberta/test-schaeffer)**

## License

- **Dataset & Audio Files:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) Attribution License
- **Code:** GPL License


## Generate Sounds with Baseline Model

Use our baseline model to generate sounds from text descriptions:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1X688Jqzq_EyNugP8GO5hctqOs0Sr-ll5?usp=sharing)

Generated audio samples with their corresponding textual captions can be found in:
```
generation/audio_samples/
```

## Training Notebook

Train your own models using our provided notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mauriziobrt/SCHAEFFER/blob/main/generation/dataset_riffusion.ipynb)

Follow the instructions in the notebook.

## Dataset Splits & K-Fold Cross-Validation

Due to the dataset's multitask learning design and large number of categories, creating balanced splits across all 1,000 sounds is challenging. Instead of providing fixed splits, we offer a flexible script that generates K-fold splits based on specified categories or features.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tyBqCR7kBN30bdpDpdihrcun4X_kRltI?usp=sharing)

## Citation

If you use the SCHAEFFER dataset in your research, please cite:

```bibtex
@inproceedings{berta2025SCHAEFFER,
  title = {{{SCHAEFFER}}: A Dataset of Human-Annotated Sound Objects for Machine Learning Applications},
  booktitle = {Proceedings of the 28 Th {{International Conference}} on {{Digital Audio Effects}}},
  author = {Berta, Maurizio and Ghisi, Daniele},
  year = 2025,
  abstract = {Machine learning for sound generation is rapidly expanding within the computer music community. However, most datasets used to train models are built from field recordings, foley sounds, instrumental notes, or commercial music. This presents a significant limitation for composers working in acousmatic and electroacoustic music, who require datasets tailored to their creative processes. To address this gap, we introduce the SCHAEFFER Dataset (Spectromorphological Corpus of Human-annotated Audio with Electroacoustic Features For Experimental Research), a curated collection of 1000 sound objects designed and annotated by composers and students of electroacoustic composition. The dataset, distributed under Creative Commons licenses, features annotations combining technical and poetic descriptions, alongside classifications based on pre-defined spectromorphological categories.},
}

```

## Contributing

We welcome contributions to improve the dataset and associated tools. Please feel free to submit issues or pull requests.

## Contact

For questions or collaborations, please contact the authors through their institutional affiliations.

