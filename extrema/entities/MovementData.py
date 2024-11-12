class Movement_Data:
    time = 0.0
    pelvis_tilt = 0.0
    pelvis_list = 0.0
    pelvis_rotation = 0.0
    pelvis_tx = 0.0
    pelvis_ty = 0.0
    pelvis_tz = 0.0
    hip_flexion_r = 0.0
    hip_adduction_r = 0.0
    hip_rotation_r = 0.0
    knee_angle_r = 0.0
    ankle_angle_r = 0.0
    subtalar_angle_r = 0.0
    mtp_angle_r = 0.0
    hip_flexion_l = 0.0
    hip_adduction_l = 0.0
    hip_rotation_l = 0.0
    knee_angle_l = 0.0
    ankle_angle_l = 0.0
    subtalar_angle_l = 0.0
    mtp_angle_l = 0.0
    lumbar_extension = 0.0
    lumbar_bending = 0.0
    lumbar_rotation = 0.0
    arm_flex_r = 0.0
    arm_add_r = 0.0
    arm_rot_r = 0.0
    elbow_flex_r = 0.0
    pro_sup_r = 0.0
    arm_flex_l = 0.0
    arm_add_l = 0.0
    arm_rot_l = 0.0
    elbow_flex_l = 0.0
    pro_sup_l = 0.0

    def __init__(self, time,
                 pelvis_tilt, pelvis_list, pelvis_rotation, pelvis_tx, pelvis_ty, pelvis_tz, hip_flexion_r,
                 hip_adduction_r,
                 hip_rotation_r, knee_angle_r, ankle_angle_r, subtalar_angle_r, mtp_angle_r, hip_flexion_l,
                 hip_adduction_l,
                 hip_rotation_l, knee_angle_l, ankle_angle_l, subtalar_angle_l, mtp_angle_l, lumbar_extension,
                 lumbar_bending,
                 lumbar_rotation, arm_flex_r, arm_add_r, arm_rot_r, elbow_flex_r, pro_sup_r, arm_flex_l, arm_add_l,
                 arm_rot_l,
                 elbow_flex_l, pro_sup_l):
        self.time = time
        self.pelvis_tilt = pelvis_tilt
        self.pelvis_list = pelvis_list
        self.pelvis_rotation = pelvis_rotation
        self.pelvis_tx = pelvis_tx
        self.pelvis_ty = pelvis_ty
        self.pelvis_tz = pelvis_tz
        self.hip_flexion_r = hip_flexion_r
        self.hip_adduction_r = hip_adduction_r
        self.hip_rotation_r = hip_rotation_r
        self.knee_angle_r = knee_angle_r
        self.ankle_angle_r = ankle_angle_r
        self.subtalar_angle_r = subtalar_angle_r
        self.mtp_angle_r = mtp_angle_r
        self.hip_flexion_l = hip_flexion_l
        self.hip_adduction_l = hip_adduction_l
        self.hip_rotation_l = hip_rotation_l
        self.knee_angle_l = knee_angle_l
        self.ankle_angle_l = ankle_angle_l
        self.subtalar_angle_l = subtalar_angle_l
        self.mtp_angle_l = mtp_angle_l
        self.lumbar_extension = lumbar_extension
        self.lumbar_bending = lumbar_bending
        self.lumbar_rotation = lumbar_rotation
        self.arm_flex_r = arm_flex_r
        self.arm_add_r = arm_add_r
        self.arm_rot_r = arm_rot_r
        self.elbow_flex_r = elbow_flex_r
        self.pro_sup_r = pro_sup_r
        self.arm_flex_l = arm_flex_l
        self.arm_add_l = arm_add_l
        self.arm_rot_l = arm_rot_l
        self.elbow_flex_l = elbow_flex_l
        self.pro_sup_l = pro_sup_l

    def get_as_dictionary(self):
        local_dict = {'pelvis_tilt': self.pelvis_tilt, 'pelvis_list': self.pelvis_list,
                      'pelvis_rotation': self.pelvis_rotation, 'pelvis_tx': self.pelvis_tx, 'pelvis_ty': self.pelvis_ty,
                      'pelvis_tz': self.pelvis_tz, 'hip_flexion_r': self.hip_flexion_r,
                      'hip_adduction_r': self.hip_adduction_r, 'hip_rotation_r': self.hip_rotation_r,
                      'knee_angle_r': self.knee_angle_r, 'ankle_angle_r': self.ankle_angle_r,
                      'subtalar_angle_r': self.subtalar_angle_r, 'mtp_angle_r': self.mtp_angle_r,
                      'hip_flexion_l': self.hip_flexion_l, 'hip_adduction_l': self.hip_adduction_l,
                      'hip_rotation_l': self.hip_rotation_l, 'knee_angle_l': self.knee_angle_l,
                      'ankle_angle_l': self.ankle_angle_l, 'subtalar_angle_l': self.subtalar_angle_l,
                      'mtp_angle_l': self.mtp_angle_l, 'lumbar_extension': self.lumbar_extension,
                      'lumbar_bending': self.lumbar_bending, 'lumbar_rotation': self.lumbar_rotation,
                      'arm_flex_r': self.arm_flex_r, 'arm_add_r': self.arm_add_r, 'arm_rot_r': self.arm_rot_r,
                      'elbow_flex_r': self.elbow_flex_r, 'pro_sup_r': self.pro_sup_r, 'arm_flex_l': self.arm_flex_l,
                      'arm_add_l': self.arm_add_l, 'arm_rot_l': self.arm_rot_l, 'elbow_flex_l': self.elbow_flex_l,
                      'pro_sup_l': self.pro_sup_l}

        return local_dict
