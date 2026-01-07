export const createNotesPanel = ({ container, onChange }) => {
  const textarea = document.createElement("textarea");
  textarea.className = "notes__textarea";
  textarea.placeholder = "Ajoutez vos notes pour cette section...";

  const helper = document.createElement("p");
  helper.className = "notes__helper";
  helper.textContent = "Les notes sont enregistrées automatiquement.";

  textarea.addEventListener("input", (event) => {
    onChange(event.target.value);
  });

  container.innerHTML = "";
  container.append(textarea, helper);

  return {
    setValue(value) {
      textarea.value = value ?? "";
    },
    focus() {
      textarea.focus();
    },
  };
};
