local full = import "full.jsonnet";

full + {
  "train_data_path": "data/train-predictions-toy.json",
  "validation_data_path": "data/valid-predictions-toy.json",
}