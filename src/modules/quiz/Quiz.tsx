import React from 'react';

import { EmptyState } from '../../components/EmptyState';
import { ErrorState } from '../../components/ErrorState';
import { LoadingSkeleton } from '../../components/LoadingSkeleton';
import { LoadState } from '../../ui/states';

interface QuizProps {
  state: LoadState;
  onRetry?: () => void;
}

export function Quiz({ state, onRetry }: QuizProps) {
  if (state === 'loading') {
    return <LoadingSkeleton lines={5} />;
  }

  if (state === 'error') {
    return <ErrorState title="Quiz indisponible" message="Impossible de récupérer les questions." onRetry={onRetry} />;
  }

  if (state === 'empty') {
    return (
      <EmptyState
        title="Aucun quiz disponible"
        description="Ajoutez un quiz pour évaluer vos connaissances."
        actionLabel="Créer un quiz"
        onAction={onRetry}
      />
    );
  }

  return (
    <section>
      <h2>Quiz</h2>
      <p>Les questions sont prêtes.</p>
    </section>
  );
}
