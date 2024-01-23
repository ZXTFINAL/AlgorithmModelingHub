<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="AlgorithmModelingHub" />

  &#xa0;

  <!-- <a href="https://AlgorithmModelingHub.netlify.app">Demo</a> -->
</div>

<h1 align="center">AlgorithmModelingHub</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ZXTFINAL/AlgorithmModelingHub?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ZXTFINAL/AlgorithmModelingHub?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ZXTFINAL/AlgorithmModelingHub?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/ZXTFINAL/AlgorithmModelingHub?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/ZXTFINAL/AlgorithmModelingHub?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/ZXTFINAL/AlgorithmModelingHub?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/ZXTFINAL/AlgorithmModelingHub?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  AlgorithmModelingHub 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/ZXTFINAL" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Modeling Templates（建模模板汇总）
本项目主要提供PyTorch的代码实现，便于读者阅读
欢迎共创的算法工程，提供不同大类下的不同行业的模型建模模板与思路，以及专利、文章的创新点思路。
目前从CV方向开始更新

正在更新backbone. . . . . .


## :sparkles: Features ##

:heavy_check_mark: 通用业务场景的不同选择;\
:heavy_check_mark: 快速建模部署;\
:heavy_check_mark: 知识汇总;

## :rocket: Technologies ##

The following tools were used in this project:

- [python](https://www.python.org/)
- [pytorch](https://www.python.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting ##

```bash
一.卷积结构
1.LeNet:
1998年 采用的sigmoid激活函数，2个Conv2d层和3个FC层
LeNet5(
  (Conv_1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
  (Sigmoid_1): Sigmoid()
  (pooling_1): AvgPool2d(kernel_size=2, stride=2, padding=0)
  (Conv_2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
  (Sigmoid_2): Sigmoid()
  (pooling_2): AvgPool2d(kernel_size=2, stride=2, padding=0)
  (Fc_1): Linear(in_features=400, out_features=120, bias=True)
  (Sigmoid_3): Sigmoid()
  (Fc_2): Linear(in_features=120, out_features=84, bias=True)
  (Sigmoid_4): Sigmoid()
  (Fc_3): Linear(in_features=84, out_features=10, bias=True)
)
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 6, 28, 28]             156
           Sigmoid-2            [-1, 6, 28, 28]               0
         AvgPool2d-3            [-1, 6, 14, 14]               0
            Conv2d-4           [-1, 16, 10, 10]           2,416
           Sigmoid-5           [-1, 16, 10, 10]               0
         AvgPool2d-6             [-1, 16, 5, 5]               0
            Linear-7                  [-1, 120]          48,120
           Sigmoid-8                  [-1, 120]               0
            Linear-9                   [-1, 84]          10,164
          Sigmoid-10                   [-1, 84]               0
           Linear-11                   [-1, 10]             850
================================================================
Total params: 61,706
Trainable params: 61,706
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.11
Params size (MB): 0.24
Estimated Total Size (MB): 0.35

二.纯注意力结构
三.混合结构
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/ZXTFINAL" target="_blank">ZXTFINAL</a>

&#xa0;

<a href="#top">Back to top</a>
