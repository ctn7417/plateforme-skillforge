import type { TaskItem } from "../api/contracts";

type TaskSection = {
  title: string;
  items: TaskItem[];
};

type TasksProps = {
  overdue: TaskItem[];
  today: TaskItem[];
  week: TaskItem[];
};

const renderTaskList = (section: TaskSection) => (
  <div className="task-section" key={section.title}>
    <h3>{section.title}</h3>
    {section.items.length === 0 ? (
      <p className="task-empty">Aucune tâche.</p>
    ) : (
      <ul>
        {section.items.map((task) => (
          <li key={task.id} className="task-item">
            <div>
              <p className="task-title">{task.title}</p>
              <p className="task-meta">
                Échéance : {task.dueAt}
                {task.courseTitle ? ` • ${task.courseTitle}` : ""}
              </p>
            </div>
          </li>
        ))}
      </ul>
    )}
  </div>
);

export const Tasks = ({ overdue, today, week }: TasksProps) => (
  <section aria-labelledby="tasks-title">
    <header>
      <h2 id="tasks-title">Tâches</h2>
      <p>Priorisez vos prochaines actions.</p>
    </header>
    <div className="tasks-grid">
      {renderTaskList({ title: "En retard", items: overdue })}
      {renderTaskList({ title: "Aujourd'hui", items: today })}
      {renderTaskList({ title: "Cette semaine", items: week })}
    </div>
  </section>
);
