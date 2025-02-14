import axios from 'axios';
import { formatData } from './formatData';

const API_URL = 'http://localhost:8000';

export interface Job {
  id: number;
  title: string;
  url: string;
  keywords: string;
  description: string;
  status: 'pending' | 'applied' | 'rejected' | 'irrelevant';
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
