#!/usr/bin/env bash

# Brown University CSCI 2470: Deep Learning (Fall 2026)
#
# Adapted from the minllama-assignment by Vijay Viswanathan, developed for
# Carnegie Mellon University's CS11-711 Advanced NLP (Graham Neubig).
# Original repository: https://github.com/neubig/minllama-assignment
#
# This script configures the environment for the Llama2 assignment.

# Download pretrained model
echo "Downloading pretrained model (stories42M.pt)..."
wget https://www.cs.cmu.edu/~vijayv/stories42M.pt

echo "Setup complete!"