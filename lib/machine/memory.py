from .utils import get, grep


class Memory:
	@staticmethod
	def get_usage():
		meminfo = get("/proc/meminfo")
		total = int(grep(meminfo, "MemTotal:"))
		available = int(grep(meminfo, "MemAvailable:"))
		cached = int(grep(meminfo, "Cached:"))
		swap_total = int(grep(meminfo, "SwapTotal:"))
		swap_available = int(grep(meminfo, "SwapFree:"))

		return {
			"total": round(1024 * total / 1000),
			"available": round(1024 * available / 1000),
			"cached": round(1024 * cached / 1000),
			"swap_total": round(1024 * swap_total / 1000),
			"swap_available": round(1024 * swap_available / 1000)
		}
