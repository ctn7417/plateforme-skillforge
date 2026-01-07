import React from 'react';

import { EmptyState } from '../../components/EmptyState';
import { ErrorState } from '../../components/ErrorState';
import { LoadingSkeleton } from '../../components/LoadingSkeleton';
import { LoadState } from '../../ui/states';

interface ReaderProps {
  state: LoadState;
  onRetry?: () => void;
}

export function Reader({ state, onRetry }: ReaderProps) {
  if (state === 'loading') {
    return <LoadingSkeleton lines={6} />;
  }

  if (state === 'error') {
    return <ErrorState title="Erreur de chargement" message="Le contenu du cours est indisponible." onRetry={onRetry} />;
  }

  if (state === 'empty') {
    return (
      <EmptyState
        title="Aucun contenu à lire"
        description="Ajoutez un module pour commencer votre lecture."
        actionLabel="Ajouter un module"
        onAction={onRetry}
      />
    );
  }

  return (
    <article>
      <h2>Lecture en cours</h2>
      <p>Voici le contenu du cours.</p>
    </article>
  );
}
