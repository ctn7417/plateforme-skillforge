import React from 'react';

interface ErrorStateProps {
  title: string;
  message?: string;
  retryLabel?: string;
  onRetry?: () => void;
}

export function ErrorState({ title, message, retryLabel = 'Réessayer', onRetry }: ErrorStateProps) {
  return (
    <section role="alert">
      <h2>{title}</h2>
      {message ? <p>{message}</p> : null}
      {onRetry ? (
        <button type="button" onClick={onRetry}>
          {retryLabel}
        </button>
      ) : null}
    </section>
  );
}
