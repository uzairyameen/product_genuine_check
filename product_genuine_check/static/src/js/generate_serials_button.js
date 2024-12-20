/** @odoo-module */
import { patch } from '@web/core/utils/patch';
import { ListController } from '@web/views/list/list_controller';

patch(ListController.prototype, {
    async openWizard(event) {
        event.preventDefault();
        event.stopPropagation();

        try {
            const actionService = this.env.services.action;

            await actionService.doAction({
                type: 'ir.actions.act_window',
                res_model: 'generate.serials.wizard',
                name: 'Generate Serial Numbers Wizard',
                view_mode: 'form',
                views: [[false, 'form']],
                target: 'new',
            });
        } catch (error) {
            console.error('Error opening wizard:', error);
        }
    },
});





















