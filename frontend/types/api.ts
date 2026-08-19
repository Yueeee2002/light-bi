/** 与后端统一的响应结构 */
export interface ApiResponse<T = unknown> {
  code: number;
  message: string;
  data: T;
}

export type UserRole = "admin" | "analyst" | "viewer";

export interface UserInfo {
  id: number;
  username: string;
  role: UserRole;
}
