frappe.ui.form.on("Material Request", "refresh", function(frm) {
    frm.add_custom_button(__('Work Order'), () => cur_frm.make_work_order(), __('Make'));
});