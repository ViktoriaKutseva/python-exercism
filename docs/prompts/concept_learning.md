## Concept Learning Prompt
**Purpose:** Universal prompt for learning and explaining complicated technical concepts simply without losing accuracy.

---

I need to understand the following concept(s): **[CONCEPT NAME/TOPIC]**

**Source Documents:** [FOLDER PATH or FILE PATHS - e.g., "data/notes/*.md" or "specific-file.md"]

**Stage 1: Concept Analysis & Breakdown**

1. **Read all source documents** from the specified folder/files
2. **Search the web** for additional context about [CONCEPT] if needed
3. **Combine information** from source documents and web search

Then:

1. **One-sentence summary** - elevator pitch
2. **Why it matters** - real-world importance
3. **Use plain language** - explain like to a first-grader, define technical terms immediately, maintain accuracy

---

**Stage 2: Making It Concrete**

For each core component, provide:
1. **Relatable analogy** - everyday comparison (e.g., "A function is like a recipe")
2. **Real-world example** - concrete scenario (e.g., "When you click 'Login'...")
3. **Visual if applicable** - simple diagram/flowchart description

---

**Stage 3: Hands-On Understanding**

1. **Simple exercise** - "try this yourself" task or thought experiment
2. **2-3 common misconceptions** - explain why wrong, provide correct understanding
3. **Compare with similar concepts** - highlight key differences

---

**Stage 4: Progressive Depth**

1. **Intermediate** - how it works internally, best practices, when to use vs alternatives
2. **Advanced** - edge cases, limitations, performance tips

---

**Stage 5: Knowledge Verification**

Create 3-5 questions:
- 1-2 basic recall (definitions, key terms)
- 1-2 application (scenarios, problem-solving)
- 1 analysis (compare, evaluate, decide)

For each: provide answer with explanation, explain why wrong answers are incorrect

---

**Stage 6: Summary & Next Steps**

1. **3-5 key takeaways** - memorizable bullet points
2. **Quick reference** - one-page cheat sheet (definition, when to use, key patterns)
3. **Learning path** - what to learn next, related concepts, recommended resources

---

**Output Format:**

Save to: `[output-folder]/[concept-name].md`

**Use this structure:**
```markdown
# [Concept Name] - Explained Simply

**Category:** [Domain/Topic Area]  
**Difficulty:** [Beginner/Intermediate/Advanced]  
**Created:** [Date]

---

## What Is It? (One-Line Summary)
[Elevator pitch]

## Why It Matters
[Practical importance]

## Breaking It Down
[Chunked explanations with analogies and examples]

## How It Works
[Step-by-step process or mechanism]

## Common Mistakes
[Misconceptions and corrections]

## Try It Yourself
[Hands-on exercise]

## Going Deeper
[Intermediate and advanced insights]

## Test Your Understanding
[Verification questions]

## Quick Reference
[Cheat sheet section]

## What's Next?
[Learning path recommendations]
```

---

## Quality Requirements

✓ Understandable to someone with no background (explain like to first-grader)
✓ All technical terms defined immediately
✓ Accurate analogies and concrete examples
✓ Logical progression (simple → complex)
✓ Misconceptions addressed
✓ Practical exercise included
✓ Complete coverage of all concepts from source documents

---

## Example Usage

**Input:** 
- Concept: "Docker containers"
- Source Documents: "data/notes/containerization/*.md"
- Additional: Search web for latest Docker best practices

**Process:**
1. Read all markdown files in data/notes/containerization/
2. Search web for "Docker containers explained" and "Docker best practices 2026"
3. Combine information from both sources

**Output:** Markdown file with:
- Analogy: Containers are like shipping containers for code
- Real example: Shipping a Python app with all dependencies
- Visual: Diagram showing container vs VM
- Exercise: "Run `docker ps` and observe..."
- Common mistake: "Containers are NOT lightweight VMs"
- Quick ref: Basic docker commands cheat sheet
- All concepts from source documents explained simply


based on the prompt #file:concept_learning_prompt.md 
create lesson for 
Concept: Non-Functional Testing 
Source: #file:4 - Non-Functional Testing.md 
Search web for latest documantation and best practices on non-functional testing
Save to data/epam/module_2/generated_lessons