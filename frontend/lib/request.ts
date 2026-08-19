/**
 * Axios 请求封装：
 * - 自动附带 JWT
 * - 按统一返回体 { code, message, data } 解包
 * 业务接口将在后续阶段接入。
 */

import axios, { AxiosError, type AxiosResponse, type InternalAxiosRequestConfig } from "axios";

import type { ApiResponse } from "@/types/api";

const request = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000",
  timeout: 15000,
});

request.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  if (typeof window !== "undefined") {
    const token = window.localStorage.getItem("lightbi_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

request.interceptors.response.use(
  (response: AxiosResponse<ApiResponse>) => {
    const payload = response.data;
    if (payload && typeof payload === "object" && "code" in payload && payload.code !== 0) {
      return Promise.reject(new Error(payload.message || "请求失败"));
    }
    return response;
  },
  (error: AxiosError<ApiResponse>) => {
    const message = error.response?.data?.message || error.message || "网络错误";
    return Promise.reject(new Error(message));
  },
);

export default request;
