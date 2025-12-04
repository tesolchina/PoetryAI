#!/bin/bash
# Quick status checker for PDF conversion

echo "========================================="
echo "PDF Conversion Progress"
echo "========================================="

# Check if process is running
if ps -p $(cat /tmp/pdf_convert_pid.txt 2>/dev/null) > /dev/null 2>&1; then
    echo "Status: ✅ RUNNING"
else
    echo "Status: ⏸️  NOT RUNNING (may be finished or stopped)"
fi

echo ""
echo "Latest Activity:"
tail -15 /Users/simonwang/Documents/Usage/AIpoetry/PoetryAI/Literature/conversion_process.log

echo ""
echo "========================================="
echo "Statistics:"
completed=$(grep -c "✅ SUCCESS" /Users/simonwang/Documents/Usage/AIpoetry/PoetryAI/Literature/conversion_process.log)
errors=$(grep -c "⚠️  ISSUE" /Users/simonwang/Documents/Usage/AIpoetry/PoetryAI/Literature/conversion_process.log)
echo "Completed: $completed"
echo "Errors: $errors"
echo "Remaining: $((56 - completed))"

# Count MD files
md_count=$(find /Users/simonwang/Documents/Usage/AIpoetry/PoetryAI/Literature/md -name "*.md" -type f | wc -l | tr -d ' ')
echo "MD files created: $md_count"
echo "========================================="


