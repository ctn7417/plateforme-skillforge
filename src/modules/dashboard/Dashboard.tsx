import React from 'react';

import { EmptyState } from '../../components/EmptyState';
import { ErrorState } from '../../components/ErrorState';
import { LoadingSkeleton } from '../../components/LoadingSkeleton';
import { LoadState } from '../../ui/states';

interface DashboardProps {
  state: LoadState;
  onReload?: () => void;
}

export function Dashboard({ state, onReload }: DashboardProps) {
  if (state === 'loading') {
    return <LoadingSkeleton lines={4} />;
  }

  if (state === 'error') {
    return <ErrorState title="Impossible de charger le dashboard" message="Veuillez réessayer." onRetry={onReload} />;
  }

  if (state === 'empty') {
    return (
      <EmptyState
        title="Aucun indicateur pour le moment"
        description="Commencez un parcours pour voir votre progression."
        actionLabel="Découvrir un parcours"
        onAction={onReload}
      />
    );
  }

  return (
    <section>
      <h2>Vue d'ensemble</h2>
      <p>Vos indicateurs sont à jour.</p>
    </section>
  );
}
