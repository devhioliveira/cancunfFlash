@echo off
REM Caminho absoluto da pasta do batch
set BASEDIR=%~dp0

fastboot getvar max-sparse-size
fastboot oem fb_mode_set
fastboot flash gpt "%BASEDIR%PGPT"
fastboot flash preloader "%BASEDIR%preloader.img"
fastboot flash lk_a "%BASEDIR%lk.img"
fastboot flash tee_a "%BASEDIR%tee.img"
fastboot flash mcupm_a "%BASEDIR%mcupm.img"
fastboot flash pi_img_a "%BASEDIR%pi_img.img"
fastboot flash sspm_a "%BASEDIR%sspm.img"
fastboot flash dtbo_a "%BASEDIR%dtbo.img"
fastboot flash logo_a "%BASEDIR%logo.img"
fastboot flash spmfw_a "%BASEDIR%spmfw.img"
fastboot flash scp_a "%BASEDIR%scp.img"
fastboot flash vbmeta_a "%BASEDIR%vbmeta.img"
fastboot flash vbmeta_system_a "%BASEDIR%vbmeta_system.img"
fastboot flash md1img_a "%BASEDIR%md1img.img"
fastboot flash dpm_a "%BASEDIR%dpm.img"
fastboot flash gz_a "%BASEDIR%gz.img"
fastboot flash vcp_a "%BASEDIR%vcp.img"
fastboot flash gpueb_a "%BASEDIR%gpueb.img"
fastboot flash efuseBackup "%BASEDIR%efuse.img"
fastboot flash boot_a "%BASEDIR%boot.img"
fastboot flash vendor_boot_a "%BASEDIR%vendor_boot.img"

fastboot flash super "%BASEDIR%super.img_sparsechunk.0"
fastboot flash super "%BASEDIR%super.img_sparsechunk.1"
fastboot flash super "%BASEDIR%super.img_sparsechunk.2"
fastboot flash super "%BASEDIR%super.img_sparsechunk.3"
fastboot flash super "%BASEDIR%super.img_sparsechunk.4"
fastboot flash super "%BASEDIR%super.img_sparsechunk.5"
fastboot flash super "%BASEDIR%super.img_sparsechunk.6"
fastboot flash super "%BASEDIR%super.img_sparsechunk.7"
fastboot flash super "%BASEDIR%super.img_sparsechunk.8"
fastboot flash super "%BASEDIR%super.img_sparsechunk.9"
fastboot flash super "%BASEDIR%super.img_sparsechunk.10"
fastboot flash super "%BASEDIR%super.img_sparsechunk.11"
fastboot flash super "%BASEDIR%super.img_sparsechunk.12"
fastboot flash super "%BASEDIR%super.img_sparsechunk.13"
fastboot flash super "%BASEDIR%super.img_sparsechunk.14"
fastboot flash super "%BASEDIR%super.img_sparsechunk.15"
fastboot flash super "%BASEDIR%super.img_sparsechunk.16"
fastboot flash super "%BASEDIR%super.img_sparsechunk.17"
fastboot flash super "%BASEDIR%super.img_sparsechunk.18"

fastboot erase nvdata
fastboot erase userdata
fastboot erase metadata
fastboot erase debug_token
fastboot oem fb_mode_clear
