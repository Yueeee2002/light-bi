/**
 * 全局状态（阶段1仅预留鉴权字段，登录页在后续阶段接入）。
 */

import { create } from "zustand";

import type { UserInfo } from "@/types/api";

interface AppState {
  token: string | null;
  user: UserInfo | null;
  setAuth: (token: string, user: UserInfo) => void;
  logout: () => void;
}

const TOKEN_KEY = "lightbi_token";

export const useAppStore = create<AppState>((set) => ({
  token: typeof window === "undefined" ? null : window.localStorage.getItem(TOKEN_KEY),
  user: null,
  setAuth: (token, user) => {
    if (typeof window !== "undefined") {
      window.localStorage.setItem(TOKEN_KEY, token);
    }
    set({ token, user });
  },
  logout: () => {
    if (typeof window !== "undefined") {
      window.localStorage.removeItem(TOKEN_KEY);
    }
    set({ token: null, user: null });
  },
}));
