package io.github.hellfraud.scaletooltips.mixin;

import java.util.List;

import org.joml.Matrix3x2fStack;
import org.joml.Vector2ic;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import io.github.hellfraud.scaletooltips.TooltipScaler;
import net.minecraft.client.font.TextRenderer;
import net.minecraft.client.gui.DrawContext;
import net.minecraft.client.gui.tooltip.TooltipComponent;
import net.minecraft.client.gui.tooltip.TooltipPositioner;
import net.minecraft.util.Identifier;

@Mixin(DrawContext.class)
public abstract class DrawContextMixin {
    @Shadow
    public abstract Matrix3x2fStack getMatrices();

    @Shadow
    public abstract int getScaledWindowWidth();

    @Shadow
    public abstract int getScaledWindowHeight();

    @Inject(method = "drawTooltipImmediately(Lnet/minecraft/client/font/TextRenderer;Ljava/util/List;IILnet/minecraft/client/gui/tooltip/TooltipPositioner;Lnet/minecraft/util/Identifier;)V",
            at = @At(value = "INVOKE", target = "Lorg/joml/Matrix3x2fStack;pushMatrix()Lorg/joml/Matrix3x2fStack;", shift = At.Shift.AFTER, remap = false))
    private void scaletooltips$fit(TextRenderer textRenderer, List<TooltipComponent> components, int x, int y,
            TooltipPositioner positioner, Identifier background, CallbackInfo ci) {
        int width = 0;
        int height = components.size() == 1 ? -2 : 0;
        for (TooltipComponent component : components) {
            width = Math.max(width, component.getWidth(textRenderer));
            height += component.getHeight(textRenderer);
        }

        Vector2ic position = positioner.getPosition(getScaledWindowWidth(), getScaledWindowHeight(), x, y, width, height);
        TooltipScaler.fit(getMatrices(), position.x(), position.y(), width, height,
                getScaledWindowWidth(), getScaledWindowHeight(), x, y);
    }
}
