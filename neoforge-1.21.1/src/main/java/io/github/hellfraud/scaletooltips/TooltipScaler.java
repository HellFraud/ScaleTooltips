package io.github.hellfraud.scaletooltips;

import com.mojang.blaze3d.vertex.PoseStack;

public final class TooltipScaler {
    private TooltipScaler() {
    }

    public static void fit(PoseStack pose, int x, int y, int width, int height,
            int screenWidth, int screenHeight) {
        int boxX = x - 5;
        int boxY = y - 5;
        int boxWidth = width + 10;
        int boxHeight = height + 10;
        float scale = Math.min(1.0f, Math.min(
                (float) screenWidth / boxWidth,
                (float) screenHeight / boxHeight));

        float scaledWidth = boxWidth * scale;
        float scaledHeight = boxHeight * scale;
        float targetX = Math.clamp(boxX, 0.0f, Math.max(0.0f, screenWidth - scaledWidth));
        float targetY = Math.clamp(boxY, 0.0f, Math.max(0.0f, screenHeight - scaledHeight));

        if (scale == 1.0f && targetX == boxX && targetY == boxY) {
            return;
        }

        pose.translate(targetX, targetY, 0.0f);
        pose.scale(scale, scale, 1.0f);
        pose.translate(-boxX, -boxY, 0.0f);
    }
}
