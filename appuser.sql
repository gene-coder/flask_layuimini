/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1-appuser
 Source Server Type    : MySQL
 Source Server Version : 101003
 Source Host           : 127.0.0.1:3306
 Source Schema         : appuser

 Target Server Type    : MySQL
 Target Server Version : 101003
 File Encoding         : 65001

 Date: 15/05/2023 16:38:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_log
-- ----------------------------
DROP TABLE IF EXISTS `t_log`;
CREATE TABLE `t_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '操作id',
  `ip` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '登录账号',
  `user_id` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '操作人userid',
  `user_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '用户名',
  `op_url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '操作连接',
  `module_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '模块名称',
  `op_label` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '操作简写',
  `op_detail` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 698 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '日志记录表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_log
-- ----------------------------
INSERT INTO `t_log` VALUES (684, '127.0.0.1', '1', 'admin', '/system/permission/role', 'sa模块', '登入页面', '测试使用_用户登入了当前页面', '2023-05-15 16:04:54');
INSERT INTO `t_log` VALUES (685, '127.0.0.1', '1', 'admin', '/system/permission/menu_tree', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:04:55');
INSERT INTO `t_log` VALUES (686, '127.0.0.1', '1', 'admin', '/system/permission/role_list', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:04:55');
INSERT INTO `t_log` VALUES (687, '127.0.0.1', '1', 'admin', '/system/user/logout', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:07:29');
INSERT INTO `t_log` VALUES (688, '127.0.0.1', '2', 'duty', '/system/user/index', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:07:44');
INSERT INTO `t_log` VALUES (689, '127.0.0.1', '2', 'duty', '/system/user/nav', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:07:45');
INSERT INTO `t_log` VALUES (690, '127.0.0.1', '2', 'duty', '/welcome', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:07:45');
INSERT INTO `t_log` VALUES (691, '127.0.0.1', '2', 'duty', '/system/user/index', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:08:44');
INSERT INTO `t_log` VALUES (692, '127.0.0.1', '2', 'duty', '/system/user/nav', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:08:45');
INSERT INTO `t_log` VALUES (693, '127.0.0.1', '2', 'duty', '/welcome', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:08:45');
INSERT INTO `t_log` VALUES (694, '127.0.0.1', '2', 'duty', '/system/user/index', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:09:08');
INSERT INTO `t_log` VALUES (695, '127.0.0.1', '2', 'duty', '/system/user/nav', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:09:09');
INSERT INTO `t_log` VALUES (696, '127.0.0.1', '2', 'duty', '/welcome', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:09:09');
INSERT INTO `t_log` VALUES (697, '127.0.0.1', '2', 'duty', '/system/user/logout', 'sa模块', '操作数据', '测试使用_用户操作了数据', '2023-05-15 16:09:12');

-- ----------------------------
-- Table structure for t_menu
-- ----------------------------
DROP TABLE IF EXISTS `t_menu`;
CREATE TABLE `t_menu`  (
  `id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '菜单ID',
  `menu_name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '菜单名称',
  `parent_id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0' COMMENT '父菜单ID',
  `order_num` int(4) NULL DEFAULT 0 COMMENT '显示顺序',
  `url` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '#' COMMENT '请求地址',
  `menu_type` tinyint(4) NULL DEFAULT NULL COMMENT '菜单类型（1,目录 2,菜单 3,按钮）',
  `visible` int(1) NULL DEFAULT 1 COMMENT '菜单状态（0显示 1隐藏）',
  `perms` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '权限标识',
  `icon` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '#' COMMENT '菜单图标',
  `is_frame` int(1) NULL DEFAULT 2 COMMENT '是否外链',
  `create_by` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '创建者',
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `remark` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '菜单权限表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_menu
-- ----------------------------
INSERT INTO `t_menu` VALUES ('5', '设置', '0', 5, '#', 1, 0, NULL, 'fa fa-address-book', 2, '', '2023-03-07 17:31:31', '');
INSERT INTO `t_menu` VALUES ('54', '权限管理', '5', 4, '', 1, 0, NULL, 'fa fa-address-book', 2, '', '2023-03-04 22:59:42', '');
INSERT INTO `t_menu` VALUES ('541', '菜单管理', '54', 1, '/system/permission/menu', 1, 0, NULL, 'fa fa-address-book', 2, '', '2023-03-04 22:59:43', '');
INSERT INTO `t_menu` VALUES ('542', '角色管理', '54', 2, '/system/permission/role', 1, 0, NULL, 'fa fa-address-book', NULL, '1', '2023-03-06 10:13:58', '角色管理页面');
INSERT INTO `t_menu` VALUES ('543', '用户管理', '54', 3, '/system/permission/user', 1, 0, NULL, 'fa fa-address-book', NULL, '1', '2023-03-06 10:13:58', '用户管理页面');

-- ----------------------------
-- Table structure for t_role
-- ----------------------------
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role`  (
  `id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色ID',
  `role_name` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色名称',
  `role_key` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '角色权限字符串',
  `role_sort` int(4) NULL DEFAULT NULL COMMENT '显示顺序',
  `data_scope` int(1) NULL DEFAULT 1 COMMENT '数据范围（1：全部数据权限 2：自定数据权限）',
  `status` int(1) NULL DEFAULT NULL COMMENT '角色状态（1正常 2停用）',
  `create_by` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '创建者',
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) COMMENT '创建时间',
  `remark` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '角色信息表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_role
-- ----------------------------
INSERT INTO `t_role` VALUES ('1', '所有权限', NULL, NULL, NULL, 0, '1', '2023-05-04 11:21:48', '管理员');

-- ----------------------------
-- Table structure for t_role_menu
-- ----------------------------
DROP TABLE IF EXISTS `t_role_menu`;
CREATE TABLE `t_role_menu`  (
  `role_id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色ID',
  `menu_id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '菜单ID',
  `id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '角色和菜单关联表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_role_menu
-- ----------------------------
INSERT INTO `t_role_menu` VALUES ('1', '543', '0abde18f', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '542', '0e8fb3ba', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', 'v6PRPOby', '2cae3a3c', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '54', '40c7b2a1', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '541', '6b3b71ce', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '61', '89479d8e', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '6', '988e9318', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '2SeghC1n', 'b7ef10ac', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '55', 'c10bb238', '2023-05-04 11:21:48');
INSERT INTO `t_role_menu` VALUES ('1', '5', 'f8d1f9e9', '2023-05-04 11:21:48');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '用户ID',
  `username` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '登录账号',
  `user_note` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '用户昵称',
  `user_type` int(1) NULL DEFAULT NULL COMMENT '用户类型（1系统用户',
  `email` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '用户邮箱',
  `phone` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `sex` int(1) NULL DEFAULT NULL COMMENT '用户性别（1男 2女 3未知）',
  `avatar` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '头像路径',
  `password` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '密码',
  `salt` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '盐加密',
  `status` int(1) NULL DEFAULT 1 COMMENT '帐号状态（0正常 1禁用',
  `del_flag` int(1) NULL DEFAULT 1 COMMENT '删除标志（1代表存在 2代表删除）',
  `login_ip` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '最后登陆IP',
  `login_date` timestamp(0) NULL DEFAULT NULL COMMENT '最后登陆时间',
  `create_by` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '创建者',
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) COMMENT '创建时间',
  `remark` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '用户信息表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '管理员', 1, NULL, NULL, NULL, NULL, 'comeon', NULL, 0, 0, NULL, NULL, NULL, '2021-10-15 04:42:44', NULL);
INSERT INTO `t_user` VALUES ('2', 'duty', '值班员', 1, NULL, NULL, NULL, NULL, 'Abc@12345', NULL, 0, 0, NULL, NULL, NULL, '2021-10-28 07:18:56', '测试');
INSERT INTO `t_user` VALUES ('4', 'hczz', '测试用户', NULL, NULL, NULL, NULL, NULL, 'Abc@12345', NULL, 0, 0, NULL, NULL, '1', '2023-03-16 17:11:17', 'aaa');

-- ----------------------------
-- Table structure for t_user_role
-- ----------------------------
DROP TABLE IF EXISTS `t_user_role`;
CREATE TABLE `t_user_role`  (
  `user_id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '用户ID',
  `role_id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色ID',
  `id` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `created_at` timestamp(0) NULL DEFAULT current_timestamp(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '用户和角色关联表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_user_role
-- ----------------------------
INSERT INTO `t_user_role` VALUES ('4', '4', '0b41852d', '2023-03-17 14:28:31');
INSERT INTO `t_user_role` VALUES ('1', '1', '1', '2023-02-28 15:30:28');
INSERT INTO `t_user_role` VALUES ('2', '2', '2', '2023-02-28 15:30:28');

SET FOREIGN_KEY_CHECKS = 1;
