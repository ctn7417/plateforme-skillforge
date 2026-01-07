import type { RecentContentItem } from "../api/contracts";

type RecentContentProps = {
  items: RecentContentItem[];
  onResume: (item: RecentContentItem) => void;
};

export const RecentContent = ({ items, onResume }: RecentContentProps) => (
  <section aria-labelledby="recent-content-title">
    <header>
      <h2 id="recent-content-title">Contenus récents</h2>
      <p>Reprenez rapidement votre progression.</p>
    </header>
    <ul className="recent-content-list">
      {items.map((item) => (
        <li key={item.id} className="recent-content-item">
          <div>
            <p className="content-title">{item.title}</p>
            <p className="content-meta">
              {item.courseTitle}
              {item.chapterTitle ? ` • ${item.chapterTitle}` : ""}
            </p>
            <p className="content-meta">Dernier accès : {item.lastAccessedAt}</p>
          </div>
          <button type="button" onClick={() => onResume(item)}>
            Reprendre
          </button>
        </li>
      ))}
    </ul>
  </section>
);
