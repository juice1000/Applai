export const getStatus = (job: any) => {
  if (job['status'] === 'irrelevant') {
    return 'Irrelevant';
  } else if (job['date_applied'] !== null) {
    return 'Applied';
  } else if (job['application_letter'] !== null) {
    return 'Ready';
  } else {
    return 'Pending';
  }
};

export const formatData = (data: any) => {
  return data.map((job: any) => ({
    ...job,
    dateApplied: job['date_applied'] && new Date(job['date_applied']).toLocaleDateString(),
    applicationLetter: job['application_letter'],
    status: getStatus(job),
  }));
};
