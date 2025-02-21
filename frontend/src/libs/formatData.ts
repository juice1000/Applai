export const getStatus = (jobData: any) => {
  if (jobData['status'] === 'irrelevant') {
    return 'irrelevant';
  } else if (jobData['status'] === 'review') {
    return 'review';
  } else if (jobData['date_applied'] !== null) {
    return 'applied';
  } else if (jobData['application_letter'] !== null) {
    return 'ready';
  } else {
    return 'pending';
  }
};

export const formatData = (data: any) => {
  return data.map((jobData: any) => {
    const formattedDate = jobData['date_applied'] && jobData.date_applied.replace('_', 'T') + ':00'; // Convert to ISO format

    return {
      ...jobData,
      dateApplied: formattedDate && new Date(formattedDate).toLocaleDateString(),
      applicationLetter: jobData['application_letter'],
      contactPerson: jobData['contact_person'],
      status: getStatus(jobData),
    };
  });
};
