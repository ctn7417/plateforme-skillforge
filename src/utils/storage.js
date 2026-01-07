const STORAGE_KEY = "skillforge.learning.v1";

export const loadState = () => {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch (error) {
    console.warn("Impossible de charger la progression", error);
    return null;
  }
};

export const saveState = (state) => {
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (error) {
    console.warn("Impossible de sauvegarder la progression", error);
  }
};

export const defaultState = (initialSectionId) => ({
  activeSectionId: initialSectionId,
  completedSections: [],
  notes: {},
  readingPositions: {},
});
