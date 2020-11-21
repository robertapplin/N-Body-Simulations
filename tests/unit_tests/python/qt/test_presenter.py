# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.presenter import NBodySimulationsPresenter
from n_body_simulations.test_helpers.mock_class_helper import MockNBodySimulationsModel, MockNBodySimulationsView
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


def setup_presenter():
    view = MockNBodySimulationsView()
    model = MockNBodySimulationsModel()
    presenter = NBodySimulationsPresenter(view, model)
    return view, model, presenter


def test_that_handle_remove_body_clicked_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    view_selected_body = mocker.spy(view, 'selected_body')
    model_remove_body = mocker.spy(model, 'remove_body')
    view_remove_body = mocker.spy(view, 'remove_body')

    presenter.handle_remove_body_clicked()

    view_selected_body.assert_called_once()
    model_remove_body.assert_called_once_with("Earth")
    view_remove_body.assert_called_once_with("Earth")


def test_that_handle_add_body_clicked_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_number_of_bodies = mocker.spy(model, 'number_of_bodies')
    view_get_axes_limits = mocker.spy(view, 'get_axes_limits')
    model_add_body = mocker.spy(model, 'add_body')
    model_initial_data = mocker.spy(model, 'initial_data')
    view_add_body = mocker.spy(view, 'add_body')

    presenter.handle_add_body_clicked("Earth")

    model_number_of_bodies.assert_called_once()
    view_get_axes_limits.assert_called_once()
    model_add_body.assert_called_once()
    model_initial_data.assert_called_once()
    view_add_body.assert_called_once()


def test_that_handle_body_name_changed_calls_the_expected_methods_when_the_new_body_name_does_not_exist(mocker):
    view, model, presenter = setup_presenter()

    model_body_names = mocker.spy(model, 'body_names')
    model_set_name = mocker.spy(model, 'set_name')
    view_update_body_name = mocker.spy(view, 'update_body_name')

    presenter.handle_body_name_changed("Earth", "Sun")

    model_body_names.assert_called_once()
    model_set_name.assert_called_once_with("Earth", "Sun")
    view_update_body_name.assert_called_once_with("Earth", "Sun")


def test_that_handle_body_name_changed_calls_the_expected_methods_when_the_new_body_name_already_exists(mocker):
    view, model, presenter = setup_presenter()

    model_body_names = mocker.spy(model, 'body_names')
    view_set_name = mocker.spy(view, 'set_name')

    try:
        presenter.handle_body_name_changed("Earth", "Earth")
    except ValueError as ex:
        assert ex == "Could not change body name: The body 'Earth' already exists."

    model_body_names.assert_called_once()
    view_set_name.assert_called_once_with("Earth")


def test_that_handle_mass_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_mass = mocker.spy(model, 'set_mass')

    presenter.handle_mass_changed("Earth", 1.0)

    model_set_mass.assert_called_once_with("Earth", 1.0)


def test_that_handle_x_position_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_x_position = mocker.spy(model, 'set_x_position')
    view_update_body_position = mocker.spy(view, 'update_body_position')

    presenter.handle_x_position_changed("Earth", 0.0)

    model_set_x_position.assert_called_once_with("Earth", 0.0)
    view_update_body_position.assert_called_once()


def test_that_handle_y_position_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_y_position = mocker.spy(model, 'set_y_position')
    view_update_body_position = mocker.spy(view, 'update_body_position')

    presenter.handle_y_position_changed("Earth", 0.0)

    model_set_y_position.assert_called_once_with("Earth", 0.0)
    view_update_body_position.assert_called_once()


def test_that_handle_x_velocity_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_x_velocity = mocker.spy(model, 'set_x_velocity')
    view_update_body_velocity = mocker.spy(view, 'update_body_velocity')

    presenter.handle_x_velocity_changed("Earth", 0.0)

    model_set_x_velocity.assert_called_once_with("Earth", 0.0)
    view_update_body_velocity.assert_called_once()


def test_that_handle_y_velocity_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_y_velocity = mocker.spy(model, 'set_y_velocity')
    view_update_body_velocity = mocker.spy(view, 'update_body_velocity')

    presenter.handle_y_velocity_changed("Earth", 0.0)

    model_set_y_velocity.assert_called_once_with("Earth", 0.0)
    view_update_body_velocity.assert_called_once()


def test_that_handle_time_step_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_time_step = mocker.spy(model, 'set_time_step')

    presenter.handle_time_step_changed(1.0)

    model_set_time_step.assert_called_once_with(1.0)


def test_that_handle_duration_changed_calls_the_expected_methods(mocker):
    view, model, presenter = setup_presenter()

    model_set_duration = mocker.spy(model, 'set_duration')

    presenter.handle_duration_changed(500.0)

    model_set_duration.assert_called_once_with(500.0)


def test_that_handle_play_pause_clicked_will_set_as_playing(mocker):
    view, model, presenter = setup_presenter()

    view_is_simulating = mocker.spy(view, 'is_simulating')
    view_set_as_playing = mocker.spy(view, 'set_as_playing')

    presenter.handle_play_pause_clicked()

    view_is_simulating.assert_called_once()
    view_set_as_playing.assert_called_once_with(True)


def test_that_handle_play_pause_clicked_will_run_the_simulation(mocker):
    view, model, presenter = setup_presenter()

    model_has_data_changed = mocker.spy(model, 'has_data_changed')
    view_stop_simulation = mocker.spy(view, 'stop_simulation')
    model_run_simulation = mocker.spy(model, 'run_simulation')

    presenter.handle_play_pause_clicked()

    model_has_data_changed.assert_called_once()
    view_stop_simulation.assert_called_once()
    model_run_simulation.assert_called_once()


def test_that_handle_body_moved_will_set_the_position_in_the_model(mocker):
    view, model, presenter = setup_presenter()

    model_set_x_position = mocker.spy(model, 'set_x_position')
    model_set_y_position = mocker.spy(model, 'set_y_position')

    presenter.handle_body_moved("Earth", 0.0, 0.0)

    model_set_x_position.assert_called_once_with("Earth", 0.0)
    model_set_y_position.assert_called_once_with("Earth", 0.0)


def test_that_handle_body_velocity_changed_will_set_the_velocity_in_the_model(mocker):
    view, model, presenter = setup_presenter()

    model_set_x_velocity = mocker.spy(model, 'set_x_velocity')
    model_set_y_velocity = mocker.spy(model, 'set_y_velocity')

    presenter.handle_body_velocity_changed("Earth", 0.0, 0.0)

    model_set_x_velocity.assert_called_once_with("Earth", 0.0)
    model_set_y_velocity.assert_called_once_with("Earth", 0.0)
