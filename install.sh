#!/bin/bash

# Make sure to run this script directly from within the project folder.

CURRENT_DIR=$(pwd)
DEST_DIR="$HOME/.local/bin"

mkdir -p "$DEST_DIR"

cat <<EOF > "$DEST_DIR/hustle"
#!/bin/bash
cd "$CURRENT_DIR"
python3 main.py "\$@"
EOF

chmod +x "$DEST_DIR/hustle"

if [[ ":$PATH:" != *":$DEST_DIR:"* ]]; then
    echo "The directory $DEST_DIR is not in your PATH."
    echo "Please add the following line to your shell configuration file (~/.bashrc or ~/.zshrc):"
    echo 'export PATH="$HOME/.local/bin:$PATH"'
fi
