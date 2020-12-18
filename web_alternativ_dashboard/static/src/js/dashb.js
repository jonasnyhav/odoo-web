odoo.define('widget_js.main', function (require) {
    const AbstractAction = require('web.AbstractAction');
    //console.log(AbstractAction);

    const core = require('web.core');

    const OurAction = AbstractAction.extend({
        start: function() {
            //this.$el.html('hello');
            this.$el.find('.widgen-dashb').click(function () {
                $('.card-success').fadeToggle();
            });
        },
        template: "js_widget_dashb.ClientAction",
        info: "This message comes from the JS"
    });

    core.action_registry.add('js_widget_dashb.action', OurAction);
});
