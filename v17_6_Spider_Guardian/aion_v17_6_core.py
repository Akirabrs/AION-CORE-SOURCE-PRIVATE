
import numpy as np

class TitanGuardian_v17_6:
    def __init__(self, limit_z=0.015):
        self.z_mem, self.v_mem = 0.0, 0.0
        self.limit_z = limit_z
        self.dt = 1e-5

    def audit(self, z_pi_pod, v_est, u_aion):
        z_expected = self.z_mem + self.v_mem * self.dt
        divergence = abs(z_pi_pod - z_expected)
        if divergence > 0.003 or abs(z_pi_pod) > self.limit_z:
            return True, -np.sign(z_pi_pod) * 200.0
        return False, u_aion

    def update_memory(self, z, v):
        self.z_mem, self.v_mem = z, v

class AionCore_v17_6_Spider:
    def __init__(self, gamma=2800.0):
        self.dt = 1e-5
        self.gamma = gamma
        self.guardian = TitanGuardian_v17_6()

    def clock_cycle(self, z_sensor, i_sensor):
        z_fast = z_sensor
        v_est = (z_fast - self.guardian.z_mem) / self.dt
        u_adaptive = -(600000 * z_fast + 15000 * v_est)
        panic, u_final = self.guardian.audit(z_fast, v_est, u_adaptive)
        self.guardian.update_memory(z_fast, v_est)
        return np.clip(u_final, -200, 200), panic
