package io.github.hellfraud.scaletooltips;

import org.joml.Matrix3x2fStack;

public final class TooltipScaler {
    private TooltipScaler() {
    }

    public static void fit(Matrix3x2fStack pose, int x, int y, int width, int height,
            int screenWidth, int screenHeight, int mouseX) {
        int boxX = x - 12;
        int boxY = y - 12;
        int boxWidth = width + 24;
        int boxHeight = height + 24;
        float scale = Math.min(1.0f, Math.min(
                (float) screenWidth / boxWidth,
                (float) screenHeight / boxHeight));

        float scaledWidth = boxWidth * scale;
        float scaledHeight = boxHeight * scale;
        int anchorX = scale < 1.0f ? mouseX + 12 : boxX;
        float targetX = Math.clamp(anchorX, 0.0f, Math.max(0.0f, screenWidth - scaledWidth));
        float targetY = scale < 1.0f ? (screenHeight - scaledHeight) * 0.5f : boxY;

        if (scale == 1.0f && targetX == boxX && targetY == boxY) {
            return;
        }

        pose.translate(targetX, targetY);
        pose.scale(scale, scale);
        pose.translate(-boxX, -boxY);
    }
}
