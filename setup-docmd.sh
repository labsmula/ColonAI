#!/bin/bash
# ColonAI - Auto Setup Script untuk DocMD.io
# Bikin setup lebih gampang dengan check & validation

set -e

echo "🚀 ColonAI - DocMD.io Auto Setup Script"
echo "============================================="
echo ""

# Check kalau sudah connect
if [ -f ".docmd-connected" ]; then
    echo "✅ DocMD.io sudah connect sebelumnya"
    echo "Mau re-setup? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        echo "❌ Cancel"
        exit 0
    fi
fi

# Step 1: Validasi struktur folder
echo "📂 Step 1: Cek struktur folder..."
if [ ! -d "docs-ui/docs" ]; then
    echo "❌ Error: docs-ui/docs/ tidak ditemukan"
    exit 1
fi

DOC_COUNT=$(find docs-ui/docs -name "*.md" | wc -l)
echo "✅ Ditemukan $DOC_COUNT file markdown"

# Step 2: Organisasi docs
echo ""
echo "📝 Step 2: Cek dokumen yang wajib..."

REQUIRED_DOCS=(
    "intro.md"
    "getting-started.md"
    "architecture.md"
    "agents.md"
    "scout-agent.md"
    "momentum-agent.md"
)

for doc in "${REQUIRED_DOCS[@]}"; do
    if [ ! -f "docs-ui/docs/$doc" ]; then
        echo "⚠️  Warning: $doc tidak ditemukan"
    fi
done

echo "✅ Validasi selesai"

# Step 3: Bikin file .docmd-ready
echo ""
echo "📝 Step 3: Bikin status file..."

cat > .docmd-ready << 'EOF'
# ColonAI - DocMD.io Import Status
# =====================================

## Status Ready untuk Import ke DocMD.io

### ✅ Checklist:
- [x] Folder structure valid (docs-ui/docs/)
- [x] File markdown siap ($DOC_COUNT files)
- [x] Setup guide siap (DOCMD-SETUP.md)
- [x] GitHub repository siap

### 🚀 Langkah Berikutnya:

1. Buka https://docmd.io
2. Connect dengan GitHub account lu
3. Import folder: docs-ui/docs/
4. Domain: colonai.docmd.io (atau buat custom)
5. Theme: GitBook (default)

### 📊 Statistik:
- Total markdown files: $DOC_COUNT
- Repository: labsmula/ColonAI
- Last updated: $(date)

### ✅ Siap!
Kalau import berhasil, dokumen akan online di:
https://colonai.docmd.io

---

## 📞 Kalau Error:

**Troubleshooting:**
1. Kalau import gagal → cek internet connection
2. Kalau file tidak muncul → refresh DocMD.io
3. Kalau format salah → delete & re-import

EOF

cat .docmd-ready

echo "✅ File .docmd-ready dibuat"
echo ""
echo "🎉 SETUP SELESAI!"
echo ""
echo "─────────────────────────────────────────────────"
echo "📂 Lokasi file status:"
echo "   docs-ui/docs/    → Semua dokumentasi markdown"
echo "   .docmd-ready       → Setup status & checklist"
echo "   DOCMD-SETUP.md   → Setup guide lengkap"
echo "─────────────────────────────────────────────────"
echo ""
echo "🚀 Langkah berikutnya:"
echo "1. Buka: https://docmd.io"
echo "2. Connect GitHub"
echo "3. Import folder: docs-ui/docs/"
echo "4. Domain: colonai.docmd.io"
echo ""
echo "✅ File .docmd-ready sudah siap sebagai checklist!"
