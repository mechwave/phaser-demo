import Hex from '../hex'
import { UnitAction } from './action'

export default class Teleport extends UnitAction {
  name = 'Teleport'
  description = 'Instantly teleport the unit on a free area'

  params: {}
  manaCost = 2

  performAction(target: Hex) {
    return {
      targets: [{
        unitId: this.unit.id, newPosition: target,
      }],
    }
  }

  targets() {
    const { pos } = this.unit
    return pos.range(6, 1)
      .filter(this.game.map.isIn)
      .filter(h => this.unit.canWalkOn(this.game.map.cellAt(h)))
  }
}
