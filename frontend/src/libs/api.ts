import axios from 'axios';
import { formatData } from './formatData';

const API_URL = 'http://localhost:8000';

export interface Job {
  id: number;
  title: string;
  url: string;
  keywords: string;
  description: string;
  status: string;
  dateApplied: string;
  applicationLetter: string;
}

export const fetchJobs = async (): Promise<Job[]> => {
  const response = await axios.get(`${API_URL}/jobs/`);
  return formatData(response.data);
};
