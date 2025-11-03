dataset_labels=[0,1,0,1,1,0,1]
unique_classes=set(dataset_labels)
if len(unique_classes)==2:
    print("This dataset is suitable for binary Classification")
elif len(unique_classes)>2:
    print("This dataset is suitable for multiclass Classification")
else:
    print("This dataset is not suitable for classification(only one class present)")