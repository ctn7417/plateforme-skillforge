import type { ProgressSnapshot } from "../api/contracts";

type ProgressOverviewProps = {
  progress: ProgressSnapshot;
};

const formatPercent = (value: number) => `${Math.round(value)}%`;

const formatMinutes = (value: number) => `${value} min`;

export const ProgressOverview = ({ progress }: ProgressOverviewProps) => {
  const completionLabel = formatPercent(progress.completionPercent);
  const weeklyGoalLabel = `${formatMinutes(progress.weeklyCompletedMinutes)} / ${formatMinutes(
    progress.weeklyGoalMinutes,
  )}`;

  return (
    <section aria-labelledby="progression-title">
      <header>
        <h2 id="progression-title">Progression</h2>
        <p>Suivez vos indicateurs clés pour rester motivé.</p>
      </header>
      <div className="progress-overview">
        <article className="metric-card">
          <h3>% complété</h3>
          <p className="metric-value">{completionLabel}</p>
          <p className="metric-caption">Global sur votre parcours actuel.</p>
        </article>
        <article className="metric-card">
          <h3>Streak</h3>
          <p className="metric-value">{progress.streakDays} jours</p>
          <p className="metric-caption">Série de jours consécutifs.</p>
        </article>
        <article className="metric-card">
          <h3>Objectif hebdo</h3>
          <p className="metric-value">{weeklyGoalLabel}</p>
          <p className="metric-caption">Temps d&apos;étude cette semaine.</p>
        </article>
      </div>
    </section>
  );
};
