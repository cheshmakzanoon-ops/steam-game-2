extends SceneTree
## Disposable Phase 011 scene probe; no shipping gameplay or autoload services.

func _initialize() -> void:
	call_deferred("_probe")

func _fail(message: String) -> void:
	push_error("BOOTSTRAP_PROBE_FAILED: " + message)
	quit(1)

func _probe() -> void:
	var scene_path: String = str(ProjectSettings.get_setting("application/run/main_scene", ""))
	var packed: PackedScene = load(scene_path) as PackedScene
	if packed == null:
		_fail("Main scene is missing or is not a PackedScene.")
		return
	var boot: Node = packed.instantiate()
	if not boot is Control or boot.name != &"Boot" or boot.get_script() != null:
		boot.free()
		_fail("Expected a script-free Control named Boot.")
		return
	root.add_child(boot)
	current_scene = boot
	await process_frame
	await process_frame
	var status: Label = boot.get_node_or_null("Status") as Label
	if status == null or boot.get_child_count() != 1:
		_fail("Expected exactly one status label; gameplay must not be bootstrapped here.")
		return
	if not status.text.contains("No gameplay systems loaded.") or status.size.x <= 0:
		_fail("Bootstrap label is missing or has no visible layout.")
		return
	for argument: String in OS.get_cmdline_user_args():
		if argument.begins_with("--capture="):
			if DisplayServer.get_name() == "headless":
				_fail("A capture needs a real rendering driver, not headless mode.")
				return
			await RenderingServer.frame_post_draw
			var image: Image = root.get_texture().get_image()
			var error: Error = image.save_png(argument.trim_prefix("--capture="))
			if error != OK:
				_fail("Cannot save capture: " + error_string(error))
				return
	print("BOOTSTRAP_SCENE_OK: script-free Boot; one visible status label; no gameplay.")
	quit(0)
