
# Exercise 11 – UX Factors and Quality Assurance

## 11.1 - UX Factors Overview

| Factor            | Description                                                     | FocusFlow Status |
|-------------------|------------------------------------------------------------------|------------------|
| Efficiency        | How quickly and easily users can accomplish tasks                | Input forms are short and direct. Actions like edit/delete are 1-click. |
| Dependability     | Whether users can rely on the system to behave consistently      | Status updates and actions are reliably reflected after API calls. |
| Usefulness        | How well the system supports task management needs               | Provides task creation, editing, filtering by status — core needs met. |
| Learnability      | How easy it is to understand and use without documentation       | UI is self-explanatory, minimal fields and buttons. |
| Controllability   | The ability to undo or change choices                            | Limited. No undo after deletion. |
| Responsiveness    | How promptly the interface responds to user actions              | Instant visual feedback after actions; async operations handled cleanly. |
| Trustworthiness   | Whether the UI conveys security and reliability                  | Token storage is in localStorage; no feedback about session expiry. |
| Attractiveness    | Visual appeal and layout aesthetics                              | Basic visual style; clean but not polished. |
| Familiarity       | Leverages common UI patterns users already know                  | Uses form inputs, dropdowns, and list groupings like Trello. |
| Novelty           | Offers something creatively new or emotionally engaging          | Functionally complete, but little innovation. |
| Stimulation       | Engages curiosity, interest, or enjoyment                        | No animations, gamification, or dynamic visuals. |

## 11.2 - Emotional Response <-> UX Factor Mapping

| User Phase         | Emotion             | UI/UX Support                                               |
|--------------------|---------------------|-------------------------------------------------------------|
| First Login        | Curious, uncertain  | Simple login form, but no onboarding or welcome message     |
| Creating a Task    | Focused, efficient  | Form is straightforward, minimal required inputs            |
| Viewing Tasks      | Organized           | Grouped by status with consistent styling                   |
| Editing/Deleting   | Confident, risky (Controllability) | Edit is easy, but delete is permanent without confirmation  |
| Status Changing    | Empowered (Controllability) | Dropdown allows instant status update, feels in control     |
| Multiple Tasks     | Slightly overwhelmed (Efficiency) | No pagination or collapse option; long lists grow visually dense |

## 11.3 - UX Factor Analysis for FocusFlow

### 1. Efficiency
- **Why**: Time is critical in task tracking.
- **Support**: Short forms, grouped tasks, inline editing.
- **Risk**: No bulk actions or filtering.

### 2. Learnability
- **Why**: Users expect low learning curve.
- **Support**: Familiar input types and visual grouping.
- **Risk**: Well-scoped and predictable actions.

### 3. Dependability
- **Why**: Task tools must reflect changes immediately and reliably.
- **Support**: API responses update UI.
- **Risk**: No offline mode or recovery from failed requests.

### 4. Controllability
- **Why**: Users want to feel safe experimenting.
- **Weakness**: No undo/redo, no delete confirmation dialog.
- **Fix**: Add simple confirmation or undo snackbar.

### 5. Attractiveness
- **Why**: Visual appeal builds trust and usability.
- **Current**: UI is functional but unstyled (default HTML elements).
- **Fix**: Use basic styling framework like Tailwind or Material UI.
- **Impact**: A more visually appealing UI can increase user trust and reduce perceived complexity.
