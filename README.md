# Scale Tooltips

![史蒂夫击碎超长提示框](art/cover.png)

物品 Lore 或其他提示内容太长、太高时，把整个提示框等比缩小，直到边框和内容都能完整显示在窗口内。普通大小的提示框保持原样。

这个模组只做这一件事，没有配置界面、按键、物品编辑或其他附加功能。

## 下载与安装

| Minecraft | 加载器 | Java | 模组文件 |
| --- | --- | --- | --- |
| 1.21.1 | NeoForge 21.1.x | 21+ | `scale-tooltips-neoforge-1.21.1-1.0.0.jar` |
| 1.21.8 | Fabric Loader 0.16.9+ | 21+ | `scale-tooltips-fabric-1.21.8-1.0.0.jar` |
| 26.3 | Fabric Loader 0.20.1+ | 25+ | `scale-tooltips-fabric-26.3-1.0.0.jar` |

把对应文件放进客户端的 `mods` 文件夹。Fabric 版不需要 Fabric API。

这是纯客户端模组。把它装进整合包或服务端 `mods` 文件夹也不会提供任何服务端功能；Fabric 会跳过它，NeoForge 不会注册客户端提示框逻辑。

## 构建

每个目录都是独立的 Gradle 工程。在对应目录运行：

```bat
gradlew.bat clean build
```

也可以在仓库根目录运行 `build-all.bat`。三个 JAR 会分别生成在各工程的 `build/libs`，并统一复制到 `dist`。

## 实现

提示框开始绘制前，代码读取所有 `TooltipComponent` 的原始宽高，计算包含边框后的缩放比：

```text
scale = min(1, screenWidth / tooltipWidth, screenHeight / tooltipHeight)
```

随后对同一个矩阵做平移和等比缩放，因此文字、Lore、物品提示组件和边框会一起缩小。没有溢出时不会缩放，只会对越界的边缘位置做必要修正。

三个版本分别编译，避免把 Yarn 映射、Mojang 映射或不同渲染 API 混在同一个 JAR 中。

## 致谢

提示框尺寸计算和矩阵变换思路来自 [mega12345mega/NBT-Editor](https://github.com/mega12345mega/NBT-Editor)，并参考、改写了其中的 `MixinLink#getTooltipSize`、`MixinLink#renderTooltipFromComponents` 和 `MainUtil#mapMatrices`。NBT-Editor 使用 MIT 许可证，其版权声明保留在本项目的 `LICENSE` 中。

本项目不包含 NBT-Editor 的其他功能。

## 许可证与作者

作者：**Hell_Fraud**  
源码：[github.com/HellFraud/ScaleTooltips](https://github.com/HellFraud/ScaleTooltips)  
许可证：[MIT](LICENSE)

封面由本项目绘制，生成脚本位于 `art/draw_cover.py`。
