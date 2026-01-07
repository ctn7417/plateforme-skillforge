export type ProgressSnapshot = {
  /** Percentage completion between 0 and 100. */
  completionPercent: number;
  /** Consecutive active days. */
  streakDays: number;
  /** Weekly goal in minutes of study. */
  weeklyGoalMinutes: number;
  /** Minutes completed in the current week. */
  weeklyCompletedMinutes: number;
};

export type RecentContentItem = {
  id: string;
  title: string;
  courseTitle: string;
  chapterTitle?: string;
  lastAccessedAt: string;
  resumePath: string;
};

export type RecentContentResponse = {
  items: RecentContentItem[];
};

export type TaskCategory = "overdue" | "today" | "week";

export type TaskItem = {
  id: string;
  title: string;
  dueAt: string;
  category: TaskCategory;
  courseTitle?: string;
};

export type TasksResponse = {
  items: TaskItem[];
};

export type DashboardOverviewResponse = {
  progress: ProgressSnapshot;
  recentContent: RecentContentResponse;
  tasks: TasksResponse;
};
