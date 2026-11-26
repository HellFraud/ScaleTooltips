package io.github.hellfraud.scaletooltips;

import org.joml.Matrix3x2fStack;

public final class TooltipScaler {
    private TooltipScaler() {
    }

    public static void fit(Matrix3x2fStack matrices, int x, int y, int width, int height,
            int screenWidth, int screenHeight) {
        int boxX = x - 12;
        int boxY = y - 12;
        int boxWidth = width + 24;
        int boxHeight = height + 24;
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

        matrices.translate(targetX, targetY);
        matrices.scale(scale, scale);
        matrices.translate(-boxX, -boxY);
    }
}
