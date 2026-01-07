import { courseData } from "./data/course.js";
import { createNotesPanel } from "./content/NotesPanel.js";
import { defaultState, loadState, saveState } from "./utils/storage.js";

const outlineEl = document.getElementById("course-outline");
const contentEl = document.getElementById("content");
const sectionTitleEl = document.getElementById("section-title");
const chapterLabelEl = document.getElementById("chapter-label");
const courseTitleEl = document.getElementById("course-title");
const toggleCompleteBtn = document.getElementById("toggle-complete");
const notesPanelContainer = document.getElementById("notes-panel");
const notesContextEl = document.getElementById("notes-context");
const readingProgressEl = document.getElementById("reading-progress");
const readingProgressLabelEl = document.getElementById("reading-progress-label");
const completionProgressEl = document.getElementById("completion-progress");
const completionProgressLabelEl = document.getElementById(
  "completion-progress-label",
);

const sectionIndex = new Map();
courseData.chapters.forEach((chapter) => {
  chapter.sections.forEach((section) => {
    sectionIndex.set(section.id, { ...section, chapter });
  });
});

const persistedState = loadState();
const initialSectionId =
  persistedState?.activeSectionId || courseData.chapters[0].sections[0].id;
const state = {
  ...(persistedState ?? defaultState(initialSectionId)),
};

const notesPanel = createNotesPanel({
  container: notesPanelContainer,
  onChange: (value) => {
    state.notes[state.activeSectionId] = value;
    persistState();
  },
});

const persistState = () => {
  saveState(state);
};

const isSectionComplete = (sectionId) =>
  state.completedSections.includes(sectionId);

const updateCompletionUI = () => {
  const totalSections = sectionIndex.size;
  const completed = state.completedSections.length;
  const completionPercent = totalSections
    ? Math.round((completed / totalSections) * 100)
    : 0;

  completionProgressEl.style.width = `${completionPercent}%`;
  completionProgressLabelEl.textContent = `${completionPercent} %`;
};

const updateReadingProgress = () => {
  const scrollable = contentEl.scrollHeight - contentEl.clientHeight;
  const progress = scrollable > 0 ? contentEl.scrollTop / scrollable : 0;
  const percent = Math.round(progress * 100);

  readingProgressEl.style.width = `${percent}%`;
  readingProgressLabelEl.textContent = `${percent} %`;
  contentEl.setAttribute("aria-valuenow", percent.toString());
};

const updateOutline = () => {
  outlineEl.innerHTML = "";
  courseTitleEl.textContent = courseData.title;

  courseData.chapters.forEach((chapter) => {
    const chapterEl = document.createElement("div");
    chapterEl.className = "outline__chapter";

    const chapterTitle = document.createElement("div");
    chapterTitle.className = "outline__chapter-title";
    chapterTitle.textContent = chapter.title;
    chapterEl.appendChild(chapterTitle);

    chapter.sections.forEach((section) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "outline__section";
      button.dataset.sectionId = section.id;
      button.setAttribute(
        "aria-current",
        section.id === state.activeSectionId ? "true" : "false",
      );

      const status = document.createElement("span");
      status.className = "outline__section-complete";
      if (isSectionComplete(section.id)) {
        status.classList.add("is-complete");
      }

      const label = document.createElement("span");
      label.textContent = section.title;

      button.append(status, label);
      button.addEventListener("click", () => {
        setActiveSection(section.id);
      });

      chapterEl.appendChild(button);
    });

    outlineEl.appendChild(chapterEl);
  });
};

const renderSection = () => {
  const section = sectionIndex.get(state.activeSectionId);
  if (!section) return;

  sectionTitleEl.textContent = section.title;
  chapterLabelEl.textContent = section.chapter.title;
  notesContextEl.textContent = `Notes pour: ${section.title}`;
  contentEl.innerHTML = `
    <p>${section.content}</p>
    <p>Objectif clé : ${section.title.toLowerCase()}.</p>
    <p>Astuce : notez les éléments qui vous semblent directement applicables à votre contexte.</p>
  `;

  const isComplete = isSectionComplete(section.id);
  toggleCompleteBtn.textContent = isComplete
    ? "Marqué comme terminé"
    : "Marquer comme terminée";
  toggleCompleteBtn.classList.toggle("button--primary", !isComplete);

  const savedPosition = state.readingPositions[section.id] ?? 0;
  contentEl.scrollTop = savedPosition;
  updateReadingProgress();
  notesPanel.setValue(state.notes[section.id] ?? "");
};

const setActiveSection = (sectionId) => {
  if (!sectionIndex.has(sectionId)) return;
  state.activeSectionId = sectionId;
  persistState();
  updateOutline();
  renderSection();
};

const toggleComplete = () => {
  const sectionId = state.activeSectionId;
  const completed = new Set(state.completedSections);
  if (completed.has(sectionId)) {
    completed.delete(sectionId);
  } else {
    completed.add(sectionId);
  }
  state.completedSections = Array.from(completed);
  persistState();
  updateOutline();
  updateCompletionUI();
  renderSection();
};

contentEl.addEventListener("scroll", () => {
  state.readingPositions[state.activeSectionId] = contentEl.scrollTop;
  updateReadingProgress();
  persistState();
});

toggleCompleteBtn.addEventListener("click", toggleComplete);

updateOutline();
renderSection();
updateCompletionUI();
