export function pick<T>(o: Record<string, T>, k: string): T | undefined {
  return o[k];
}

export async function fetchJson(url: string): Promise<any> {
  const r = await fetch(url);
  return r.json();
}

export const API_BASE = process.env.API_BASE ?? "https://example.com";
