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
import net.minecraft.client.gui.Font;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.screens.inventory.tooltip.ClientTooltipComponent;
import net.minecraft.client.gui.screens.inventory.tooltip.ClientTooltipPositioner;
import net.minecraft.resources.Identifier;

@Mixin(GuiGraphicsExtractor.class)
public abstract class GuiGraphicsExtractorMixin {
    @Shadow
    public abstract Matrix3x2fStack pose();

    @Shadow
    public abstract int guiWidth();

    @Shadow
    public abstract int guiHeight();

    @Inject(method = "tooltip(Lnet/minecraft/client/gui/Font;Ljava/util/List;IILnet/minecraft/client/gui/screens/inventory/tooltip/ClientTooltipPositioner;Lnet/minecraft/resources/Identifier;Z)V",
            at = @At(value = "INVOKE", target = "Lorg/joml/Matrix3x2fStack;pushMatrix()Lorg/joml/Matrix3x2fStack;", shift = At.Shift.AFTER, remap = false))
    private void scaletooltips$fit(Font font, List<ClientTooltipComponent> components, int x, int y,
            ClientTooltipPositioner positioner, Identifier background, boolean focused, CallbackInfo ci) {
        int width = 0;
        int height = components.size() == 1 || !focused ? -2 : 0;
        for (ClientTooltipComponent component : components) {
            width = Math.max(width, component.getWidth(font));
            height += component.getHeight(font);
        }

        Vector2ic position = positioner.positionTooltip(guiWidth(), guiHeight(), x, y, width, height);
        TooltipScaler.fit(pose(), position.x(), position.y(), width, height, guiWidth(), guiHeight());
    }
}
