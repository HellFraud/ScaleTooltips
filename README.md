# Scale Tooltips

![Scale Tooltips 封面](art/cover.png)

Lore 一多，物品提示框就容易冲出屏幕。Scale Tooltips 会把整个提示框按比例缩小，让文字、图标和边框都留在窗口里。普通大小的提示框不会被缩小。

模组没有配置界面，也没有其他功能，装上就生效。

## 下载

在 [Releases](https://github.com/HellFraud/ScaleTooltips/releases) 里选择对应版本：

| Minecraft | 加载器 | Java | 文件 |
| --- | --- | --- | --- |
| 1.21.1 | NeoForge 21.1.x | 21+ | `scale-tooltips-neoforge-1.21.1-1.0.0.jar` |
| 1.21.8 | Fabric Loader 0.16.9+ | 21+ | `scale-tooltips-fabric-1.21.8-1.0.0.jar` |
| 26.3 | Fabric Loader 0.20.1+ | 25+ | `scale-tooltips-fabric-26.3-1.0.0.jar` |

把文件放进客户端的 `mods` 文件夹即可。Fabric 版不需要 Fabric API。

这是客户端模组，在服务端不会生效。误放进服务端也不用紧张：Fabric 会跳过它，NeoForge 不会加载提示框逻辑，不会因此崩溃。

## 自己构建

安装 JDK 25，在仓库根目录运行：

```bat
build-all.bat
```

构建结果会汇总到 `dist`。只需要其中一个版本时，也可以进入对应目录运行 `gradlew.bat build`。

三个版本是独立的 Gradle 工程，因为它们的映射和提示框绘制方式并不相同。

## 它是怎么工作的

绘制前，代码会先量出提示框连同边框的宽高，再取窗口宽、高两个缩放比中较小的那个。文字、Lore、物品组件和边框使用同一个矩阵缩放，所以不会只缩内容而把边框留在外面。

没有超出窗口时，模组不会缩小提示框。

## 致谢

这个功能参考并改写了 [NBT-Editor](https://github.com/mega12345mega/NBT-Editor) 中提示框尺寸计算和矩阵变换的实现。NBT-Editor 使用 MIT 许可证，原作者声明保留在本项目的 `LICENSE` 中。

这里没有加入 NBT-Editor 的其他功能。

## 作者与许可证

作者：**Hell_Fraud**  
许可证：[MIT](LICENSE)

封面由 AI 绘制，史蒂夫素材来自用户提供的图片 1。
