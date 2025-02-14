export const getStatus = (jobData: any) => {
  if (jobData['status'] === 'irrelevant') {
    return 'irrelevant';
  } else if (jobData['date_applied'] !== null) {
    return 'applied';
  } else if (jobData['application_letter'] !== null) {
    return 'ready';
  } else {
    return 'pending';
  }
};

export const formatData = (data: any) => {
  return data.map((jobData: any) => ({
    ...jobData,
    dateApplied: jobData['date_applied'] && new Date(job['date_applied']).toLocaleDateString(),
    applicationLetter: jobData['application_letter'],
    status: getStatus(jobData),
  }));
};
