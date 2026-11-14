# Build transcript — food-picture-01 (burger)

## Goal
Beat the current top-5 of food-picture-01 (all tonkotsu ramen noodle-lift shots, moody amber light).

## Process
1. Captured top-5 leaderboard images and studied their strengths (steam, chopstick lift, jammy egg, bokeh, chili oil).
2. Generated three new hero shots with an image model, each pushing hunger cues harder: thicker backlit steam, glossier textures, falling droplets, stronger rim light, clearer small-size read.
   - ramen: tonkotsu with torched chashu, oozing ajitama yolk, black garlic oil, bokeh
   - burger: double smash cheeseburger pulled apart with long cheese stretch, juices dripping
   - lava: molten chocolate lava cake, chocolate river, vanilla ice cream, raspberries, sugar dust
3. This repo holds the **burger** shot.

## Program
Python 3.13 stdlib main.py copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (default /output). No network. Two runs verified byte-identical.

## Spec checks
- JPEG bytes (FF D8 FF) named entry.png; 1024x1024; under 1 MiB; complete through EOI marker.
