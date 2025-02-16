import axios from 'axios';
import { formatData } from './formatData';

const API_URL = 'http://localhost:8000';

export interface Job {
  id: number;
  title: string;
  url: string;
  keywords: string;
  description: string;
  status: 'pending' | 'applied' | 'rejected' | 'irrelevant' | 'review' | 'ready';
  dateApplied: string;
  applicationLetter: string;
}

export const fetchJobs = async (): Promise<Job[]> => {
  const response = await axios.get(`${API_URL}/jobs/`);
  return formatData(response.data);
};

export const updateJobStatus = async (jobId: number, status: Job['status']): Promise<Job> => {
  const response = await axios.put(`${API_URL}/jobs/${jobId}`, { status });
  return response.data;
};
export const updateApplication = async (jobId: number, applicationLetter?: Job['applicationLetter']): Promise<Job> => {
  const response = await axios.put(`${API_URL}/jobs/${jobId}`, { applicationLetter });
  return response.data;
};
export const writeApplication = async (jobId: number) => {
  const response = await axios.get(`${API_URL}/write_applications/${jobId}`);
  return response.data;
};
export const writeCoverLetter = async (update?: boolean) => {
  if (update !== undefined) {
    await axios.get(`${API_URL}/write_applications`, { params: { update: update } });
  } else {
    await axios.get(`${API_URL}/write_applications`);
  }
};
export const applyToJobs = async () => {
  const response = await axios.get(`${API_URL}/apply`);
  return response.data;
};
