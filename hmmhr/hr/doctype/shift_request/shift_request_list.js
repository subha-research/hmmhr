frappe.listview_settings["Shift Request"] = {
	onload: (list_view) =>
		hmmhr.add_shift_tools_button_to_list(list_view, "Process Shift Requests"),
};
