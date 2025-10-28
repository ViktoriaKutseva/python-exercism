# How to Run JavaScript Tests

This guide explains how to run tests for your JavaScript Exercism exercises.

## Prerequisites

Make sure you have Node.js installed and dependencies are installed:
```bash
npm install
```

## Running Tests

### 1. Basic Test Run
Run all tests once:
```bash
npm test
```

### 2. Watch Mode (Recommended for Development)
Run tests in watch mode - automatically re-runs tests when files change:
```bash
npm run watch
```

### 3. Using Jest Directly
If you have Jest installed globally, you can also run:
```bash
jest
```

## Test Output Explanation

### ✅ Passing Test
```
PASS  ./hello-world.spec.js
  Hello World
    ✓ Say Hi! (7 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

### ❌ Failing Test
```
FAIL  ./hello-world.spec.js
  Hello World
    ✕ Say Hi! (6 ms)

  ● Hello World › Say Hi!

    expect(received).toEqual(expected) // deep equality

    Expected: "Hello, World!"
    Received: "Hello, World"
```

## Additional Commands

### Code Linting
Check your code style:
```bash
npm run lint
```

### Code Formatting
Auto-format your code:
```bash
npm run format
```

## Tips for Test-Driven Development

1. **Start with failing tests** - Read the test file to understand requirements
2. **Run tests frequently** - Use watch mode (`npm run watch`)
3. **Make small changes** - Implement one test case at a time
4. **Check test output** - Read error messages carefully for hints

## File Structure

- `*.js` - Your implementation files
- `*.spec.js` - Test files (Jest test suites)
- `package.json` - Contains test scripts and dependencies

## Troubleshooting

### Common Issues

1. **Module not found errors**
   - Make sure you've run `npm install`
   - Check that your export/import statements are correct

2. **Tests not running**
   - Verify you're in the correct directory
   - Check that Jest is installed in `node_modules`

3. **Syntax errors**
   - Use `npm run lint` to check for code style issues
   - Make sure your JavaScript syntax is valid

### Getting Help

- Read the `README.md` file in each exercise directory
- Check the `HELP.md` file for exercise-specific guidance
- Look at the test file (`*.spec.js`) to understand expected behavior

## Example Workflow

1. Read the exercise instructions in `README.md`
2. Look at the test file to understand requirements
3. Start watch mode: `npm run watch`
4. Implement your solution in the `.js` file
5. Save and watch tests automatically run
6. Repeat until all tests pass ✅