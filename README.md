# abnormal_inspection
Trial Project

# model structure checker

```
python classmasterch.py

```
## example

```
        (stochastic_depth): StochasticDepth(p=0.195, mode=row)
      )
    )
    (7): Conv2dNormActivation(
      (0): Conv2d(256, 1280, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (1): BatchNorm2d(1280, eps=0.001, momentum=0.1, affine=True, track_running_stats=True)
      (2): SiLU(inplace=True)
    )
  )
  (avgpool): AdaptiveAvgPool2d(output_size=1)
  (classifier): Sequential(
    (0): Dropout(p=0.2, inplace=True)
    (1): Linear(in_features=1280, out_features=1000, bias=True)
  )
)
Feature vector shape: torch.Size([512000])


```

# Defective detection Project
-We need your knowledge and cooperation.
- wecolem to your support 
